// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: aws/aws_codestarconnections.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021, 8981
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace Oak9.Tython.Aws.Codestarconnections {

  /// <summary>Holder for reflection information generated from aws/aws_codestarconnections.proto</summary>
  public static partial class AwsCodestarconnectionsReflection {

    #region Descriptor
    /// <summary>File descriptor for aws/aws_codestarconnections.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static AwsCodestarconnectionsReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "CiFhd3MvYXdzX2NvZGVzdGFyY29ubmVjdGlvbnMucHJvdG8SI29hazkudHl0",
            "aG9uLmF3cy5jb2Rlc3RhcmNvbm5lY3Rpb25zGhNzaGFyZWQvc2hhcmVkLnBy",
            "b3RvIv0BCgpDb25uZWN0aW9uEjcKDXJlc291cmNlX2luZm8YASABKAsyIC5v",
            "YWs5LnR5dGhvbi5zaGFyZWQuUmVzb3VyY2VJbmZvEhcKD2Nvbm5lY3Rpb25f",
            "bmFtZRgCIAEoCRIVCg1wcm92aWRlcl90eXBlGAMgASgJEhAKCGhvc3RfYXJu",
            "GAQgASgJEkcKBHRhZ3MYBSADKAsyOS5vYWs5LnR5dGhvbi5hd3MuY29kZXN0",
            "YXJjb25uZWN0aW9ucy5Db25uZWN0aW9uLlRhZ3NFbnRyeRorCglUYWdzRW50",
            "cnkSCwoDa2V5GAEgASgJEg0KBXZhbHVlGAIgASgJOgI4ASJaChNDb2RlU3Rh",
            "ckNvbm5lY3Rpb25zEkMKCmNvbm5lY3Rpb24YASADKAsyLy5vYWs5LnR5dGhv",
            "bi5hd3MuY29kZXN0YXJjb25uZWN0aW9ucy5Db25uZWN0aW9uYgZwcm90bzM="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { global::Oak9.Tython.Shared.SharedReflection.Descriptor, },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::Oak9.Tython.Aws.Codestarconnections.Connection), global::Oak9.Tython.Aws.Codestarconnections.Connection.Parser, new[]{ "ResourceInfo", "ConnectionName", "ProviderType", "HostArn", "Tags" }, null, null, null, new pbr::GeneratedClrTypeInfo[] { null, }),
            new pbr::GeneratedClrTypeInfo(typeof(global::Oak9.Tython.Aws.Codestarconnections.CodeStarConnections), global::Oak9.Tython.Aws.Codestarconnections.CodeStarConnections.Parser, new[]{ "Connection" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class Connection : pb::IMessage<Connection>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<Connection> _parser = new pb::MessageParser<Connection>(() => new Connection());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pb::MessageParser<Connection> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Oak9.Tython.Aws.Codestarconnections.AwsCodestarconnectionsReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public Connection() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public Connection(Connection other) : this() {
      resourceInfo_ = other.resourceInfo_ != null ? other.resourceInfo_.Clone() : null;
      connectionName_ = other.connectionName_;
      providerType_ = other.providerType_;
      hostArn_ = other.hostArn_;
      tags_ = other.tags_.Clone();
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public Connection Clone() {
      return new Connection(this);
    }

    /// <summary>Field number for the "resource_info" field.</summary>
    public const int ResourceInfoFieldNumber = 1;
    private global::Oak9.Tython.Shared.ResourceInfo resourceInfo_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public global::Oak9.Tython.Shared.ResourceInfo ResourceInfo {
      get { return resourceInfo_; }
      set {
        resourceInfo_ = value;
      }
    }

    /// <summary>Field number for the "connection_name" field.</summary>
    public const int ConnectionNameFieldNumber = 2;
    private string connectionName_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string ConnectionName {
      get { return connectionName_; }
      set {
        connectionName_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "provider_type" field.</summary>
    public const int ProviderTypeFieldNumber = 3;
    private string providerType_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string ProviderType {
      get { return providerType_; }
      set {
        providerType_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "host_arn" field.</summary>
    public const int HostArnFieldNumber = 4;
    private string hostArn_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string HostArn {
      get { return hostArn_; }
      set {
        hostArn_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "tags" field.</summary>
    public const int TagsFieldNumber = 5;
    private static readonly pbc::MapField<string, string>.Codec _map_tags_codec
        = new pbc::MapField<string, string>.Codec(pb::FieldCodec.ForString(10, ""), pb::FieldCodec.ForString(18, ""), 42);
    private readonly pbc::MapField<string, string> tags_ = new pbc::MapField<string, string>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::MapField<string, string> Tags {
      get { return tags_; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override bool Equals(object other) {
      return Equals(other as Connection);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public bool Equals(Connection other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (!object.Equals(ResourceInfo, other.ResourceInfo)) return false;
      if (ConnectionName != other.ConnectionName) return false;
      if (ProviderType != other.ProviderType) return false;
      if (HostArn != other.HostArn) return false;
      if (!Tags.Equals(other.Tags)) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override int GetHashCode() {
      int hash = 1;
      if (resourceInfo_ != null) hash ^= ResourceInfo.GetHashCode();
      if (ConnectionName.Length != 0) hash ^= ConnectionName.GetHashCode();
      if (ProviderType.Length != 0) hash ^= ProviderType.GetHashCode();
      if (HostArn.Length != 0) hash ^= HostArn.GetHashCode();
      hash ^= Tags.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void WriteTo(pb::CodedOutputStream output) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      output.WriteRawMessage(this);
    #else
      if (resourceInfo_ != null) {
        output.WriteRawTag(10);
        output.WriteMessage(ResourceInfo);
      }
      if (ConnectionName.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(ConnectionName);
      }
      if (ProviderType.Length != 0) {
        output.WriteRawTag(26);
        output.WriteString(ProviderType);
      }
      if (HostArn.Length != 0) {
        output.WriteRawTag(34);
        output.WriteString(HostArn);
      }
      tags_.WriteTo(output, _map_tags_codec);
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      if (resourceInfo_ != null) {
        output.WriteRawTag(10);
        output.WriteMessage(ResourceInfo);
      }
      if (ConnectionName.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(ConnectionName);
      }
      if (ProviderType.Length != 0) {
        output.WriteRawTag(26);
        output.WriteString(ProviderType);
      }
      if (HostArn.Length != 0) {
        output.WriteRawTag(34);
        output.WriteString(HostArn);
      }
      tags_.WriteTo(ref output, _map_tags_codec);
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public int CalculateSize() {
      int size = 0;
      if (resourceInfo_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(ResourceInfo);
      }
      if (ConnectionName.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(ConnectionName);
      }
      if (ProviderType.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(ProviderType);
      }
      if (HostArn.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(HostArn);
      }
      size += tags_.CalculateSize(_map_tags_codec);
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(Connection other) {
      if (other == null) {
        return;
      }
      if (other.resourceInfo_ != null) {
        if (resourceInfo_ == null) {
          ResourceInfo = new global::Oak9.Tython.Shared.ResourceInfo();
        }
        ResourceInfo.MergeFrom(other.ResourceInfo);
      }
      if (other.ConnectionName.Length != 0) {
        ConnectionName = other.ConnectionName;
      }
      if (other.ProviderType.Length != 0) {
        ProviderType = other.ProviderType;
      }
      if (other.HostArn.Length != 0) {
        HostArn = other.HostArn;
      }
      tags_.MergeFrom(other.tags_);
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(pb::CodedInputStream input) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      input.ReadRawMessage(this);
    #else
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            if (resourceInfo_ == null) {
              ResourceInfo = new global::Oak9.Tython.Shared.ResourceInfo();
            }
            input.ReadMessage(ResourceInfo);
            break;
          }
          case 18: {
            ConnectionName = input.ReadString();
            break;
          }
          case 26: {
            ProviderType = input.ReadString();
            break;
          }
          case 34: {
            HostArn = input.ReadString();
            break;
          }
          case 42: {
            tags_.AddEntriesFrom(input, _map_tags_codec);
            break;
          }
        }
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
            break;
          case 10: {
            if (resourceInfo_ == null) {
              ResourceInfo = new global::Oak9.Tython.Shared.ResourceInfo();
            }
            input.ReadMessage(ResourceInfo);
            break;
          }
          case 18: {
            ConnectionName = input.ReadString();
            break;
          }
          case 26: {
            ProviderType = input.ReadString();
            break;
          }
          case 34: {
            HostArn = input.ReadString();
            break;
          }
          case 42: {
            tags_.AddEntriesFrom(ref input, _map_tags_codec);
            break;
          }
        }
      }
    }
    #endif

  }

  public sealed partial class CodeStarConnections : pb::IMessage<CodeStarConnections>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<CodeStarConnections> _parser = new pb::MessageParser<CodeStarConnections>(() => new CodeStarConnections());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pb::MessageParser<CodeStarConnections> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Oak9.Tython.Aws.Codestarconnections.AwsCodestarconnectionsReflection.Descriptor.MessageTypes[1]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public CodeStarConnections() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public CodeStarConnections(CodeStarConnections other) : this() {
      connection_ = other.connection_.Clone();
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public CodeStarConnections Clone() {
      return new CodeStarConnections(this);
    }

    /// <summary>Field number for the "connection" field.</summary>
    public const int ConnectionFieldNumber = 1;
    private static readonly pb::FieldCodec<global::Oak9.Tython.Aws.Codestarconnections.Connection> _repeated_connection_codec
        = pb::FieldCodec.ForMessage(10, global::Oak9.Tython.Aws.Codestarconnections.Connection.Parser);
    private readonly pbc::RepeatedField<global::Oak9.Tython.Aws.Codestarconnections.Connection> connection_ = new pbc::RepeatedField<global::Oak9.Tython.Aws.Codestarconnections.Connection>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::RepeatedField<global::Oak9.Tython.Aws.Codestarconnections.Connection> Connection {
      get { return connection_; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override bool Equals(object other) {
      return Equals(other as CodeStarConnections);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public bool Equals(CodeStarConnections other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if(!connection_.Equals(other.connection_)) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override int GetHashCode() {
      int hash = 1;
      hash ^= connection_.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void WriteTo(pb::CodedOutputStream output) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      output.WriteRawMessage(this);
    #else
      connection_.WriteTo(output, _repeated_connection_codec);
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      connection_.WriteTo(ref output, _repeated_connection_codec);
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public int CalculateSize() {
      int size = 0;
      size += connection_.CalculateSize(_repeated_connection_codec);
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(CodeStarConnections other) {
      if (other == null) {
        return;
      }
      connection_.Add(other.connection_);
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(pb::CodedInputStream input) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      input.ReadRawMessage(this);
    #else
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            connection_.AddEntriesFrom(input, _repeated_connection_codec);
            break;
          }
        }
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
            break;
          case 10: {
            connection_.AddEntriesFrom(ref input, _repeated_connection_codec);
            break;
          }
        }
      }
    }
    #endif

  }

  #endregion

}

#endregion Designer generated code