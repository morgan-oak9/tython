// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: gcp/gcp_compute_ha.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021, 8981
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace Oak9.Tython.Gcp.ComputeHa {

  /// <summary>Holder for reflection information generated from gcp/gcp_compute_ha.proto</summary>
  public static partial class GcpComputeHaReflection {

    #region Descriptor
    /// <summary>File descriptor for gcp/gcp_compute_ha.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static GcpComputeHaReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "ChhnY3AvZ2NwX2NvbXB1dGVfaGEucHJvdG8SGm9hazkudHl0aG9uLmdjcC5j",
            "b21wdXRlX2hhGhNzaGFyZWQvc2hhcmVkLnByb3RvIj4KHENvbXB1dGVIYVZw",
            "bkdhdGV3YXlYVGltZW91dHMSDgoGY3JlYXRlGAEgASgJEg4KBmRlbGV0ZRgC",
            "IAEoCSJkCiFDb21wdXRlSGFWcG5HYXRld2F5WFZwbkludGVyZmFjZXMSCgoC",
            "aWQYASABKAESHwoXaW50ZXJjb25uZWN0X2F0dGFjaG1lbnQYAiABKAkSEgoK",
            "aXBfYWRkcmVzcxgDIAEoCSLlAgoTQ29tcHV0ZUhhVnBuR2F0ZXdheRITCgtk",
            "ZXNjcmlwdGlvbhgBIAEoCRIKCgJpZBgCIAEoCRIMCgRuYW1lGAMgASgJEg8K",
            "B25ldHdvcmsYBCABKAkSDwoHcHJvamVjdBgFIAEoCRIOCgZyZWdpb24YBiAB",
            "KAkSEQoJc2VsZl9saW5rGAcgASgJEkoKCHRpbWVvdXRzGAggASgLMjgub2Fr",
            "OS50eXRob24uZ2NwLmNvbXB1dGVfaGEuQ29tcHV0ZUhhVnBuR2F0ZXdheVhU",
            "aW1lb3V0cxJVCg52cG5faW50ZXJmYWNlcxgJIAMoCzI9Lm9hazkudHl0aG9u",
            "LmdjcC5jb21wdXRlX2hhLkNvbXB1dGVIYVZwbkdhdGV3YXlYVnBuSW50ZXJm",
            "YWNlcxI3Cg1yZXNvdXJjZV9pbmZvGAogASgLMiAub2FrOS50eXRob24uc2hh",
            "cmVkLlJlc291cmNlSW5mb2IGcHJvdG8z"));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { global::Oak9.Tython.Shared.SharedReflection.Descriptor, },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::Oak9.Tython.Gcp.ComputeHa.ComputeHaVpnGatewayXTimeouts), global::Oak9.Tython.Gcp.ComputeHa.ComputeHaVpnGatewayXTimeouts.Parser, new[]{ "Create", "Delete" }, null, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::Oak9.Tython.Gcp.ComputeHa.ComputeHaVpnGatewayXVpnInterfaces), global::Oak9.Tython.Gcp.ComputeHa.ComputeHaVpnGatewayXVpnInterfaces.Parser, new[]{ "Id", "InterconnectAttachment", "IpAddress" }, null, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::Oak9.Tython.Gcp.ComputeHa.ComputeHaVpnGateway), global::Oak9.Tython.Gcp.ComputeHa.ComputeHaVpnGateway.Parser, new[]{ "Description", "Id", "Name", "Network", "Project", "Region", "SelfLink", "Timeouts", "VpnInterfaces", "ResourceInfo" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class ComputeHaVpnGatewayXTimeouts : pb::IMessage<ComputeHaVpnGatewayXTimeouts>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<ComputeHaVpnGatewayXTimeouts> _parser = new pb::MessageParser<ComputeHaVpnGatewayXTimeouts>(() => new ComputeHaVpnGatewayXTimeouts());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pb::MessageParser<ComputeHaVpnGatewayXTimeouts> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Oak9.Tython.Gcp.ComputeHa.GcpComputeHaReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public ComputeHaVpnGatewayXTimeouts() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public ComputeHaVpnGatewayXTimeouts(ComputeHaVpnGatewayXTimeouts other) : this() {
      create_ = other.create_;
      delete_ = other.delete_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public ComputeHaVpnGatewayXTimeouts Clone() {
      return new ComputeHaVpnGatewayXTimeouts(this);
    }

    /// <summary>Field number for the "create" field.</summary>
    public const int CreateFieldNumber = 1;
    private string create_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Create {
      get { return create_; }
      set {
        create_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "delete" field.</summary>
    public const int DeleteFieldNumber = 2;
    private string delete_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Delete {
      get { return delete_; }
      set {
        delete_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override bool Equals(object other) {
      return Equals(other as ComputeHaVpnGatewayXTimeouts);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public bool Equals(ComputeHaVpnGatewayXTimeouts other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (Create != other.Create) return false;
      if (Delete != other.Delete) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override int GetHashCode() {
      int hash = 1;
      if (Create.Length != 0) hash ^= Create.GetHashCode();
      if (Delete.Length != 0) hash ^= Delete.GetHashCode();
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
      if (Create.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(Create);
      }
      if (Delete.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(Delete);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      if (Create.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(Create);
      }
      if (Delete.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(Delete);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public int CalculateSize() {
      int size = 0;
      if (Create.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Create);
      }
      if (Delete.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Delete);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(ComputeHaVpnGatewayXTimeouts other) {
      if (other == null) {
        return;
      }
      if (other.Create.Length != 0) {
        Create = other.Create;
      }
      if (other.Delete.Length != 0) {
        Delete = other.Delete;
      }
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
            Create = input.ReadString();
            break;
          }
          case 18: {
            Delete = input.ReadString();
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
            Create = input.ReadString();
            break;
          }
          case 18: {
            Delete = input.ReadString();
            break;
          }
        }
      }
    }
    #endif

  }

  public sealed partial class ComputeHaVpnGatewayXVpnInterfaces : pb::IMessage<ComputeHaVpnGatewayXVpnInterfaces>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<ComputeHaVpnGatewayXVpnInterfaces> _parser = new pb::MessageParser<ComputeHaVpnGatewayXVpnInterfaces>(() => new ComputeHaVpnGatewayXVpnInterfaces());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pb::MessageParser<ComputeHaVpnGatewayXVpnInterfaces> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Oak9.Tython.Gcp.ComputeHa.GcpComputeHaReflection.Descriptor.MessageTypes[1]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public ComputeHaVpnGatewayXVpnInterfaces() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public ComputeHaVpnGatewayXVpnInterfaces(ComputeHaVpnGatewayXVpnInterfaces other) : this() {
      id_ = other.id_;
      interconnectAttachment_ = other.interconnectAttachment_;
      ipAddress_ = other.ipAddress_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public ComputeHaVpnGatewayXVpnInterfaces Clone() {
      return new ComputeHaVpnGatewayXVpnInterfaces(this);
    }

    /// <summary>Field number for the "id" field.</summary>
    public const int IdFieldNumber = 1;
    private double id_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public double Id {
      get { return id_; }
      set {
        id_ = value;
      }
    }

    /// <summary>Field number for the "interconnect_attachment" field.</summary>
    public const int InterconnectAttachmentFieldNumber = 2;
    private string interconnectAttachment_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string InterconnectAttachment {
      get { return interconnectAttachment_; }
      set {
        interconnectAttachment_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "ip_address" field.</summary>
    public const int IpAddressFieldNumber = 3;
    private string ipAddress_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string IpAddress {
      get { return ipAddress_; }
      set {
        ipAddress_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override bool Equals(object other) {
      return Equals(other as ComputeHaVpnGatewayXVpnInterfaces);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public bool Equals(ComputeHaVpnGatewayXVpnInterfaces other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (!pbc::ProtobufEqualityComparers.BitwiseDoubleEqualityComparer.Equals(Id, other.Id)) return false;
      if (InterconnectAttachment != other.InterconnectAttachment) return false;
      if (IpAddress != other.IpAddress) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override int GetHashCode() {
      int hash = 1;
      if (Id != 0D) hash ^= pbc::ProtobufEqualityComparers.BitwiseDoubleEqualityComparer.GetHashCode(Id);
      if (InterconnectAttachment.Length != 0) hash ^= InterconnectAttachment.GetHashCode();
      if (IpAddress.Length != 0) hash ^= IpAddress.GetHashCode();
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
      if (Id != 0D) {
        output.WriteRawTag(9);
        output.WriteDouble(Id);
      }
      if (InterconnectAttachment.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(InterconnectAttachment);
      }
      if (IpAddress.Length != 0) {
        output.WriteRawTag(26);
        output.WriteString(IpAddress);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      if (Id != 0D) {
        output.WriteRawTag(9);
        output.WriteDouble(Id);
      }
      if (InterconnectAttachment.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(InterconnectAttachment);
      }
      if (IpAddress.Length != 0) {
        output.WriteRawTag(26);
        output.WriteString(IpAddress);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public int CalculateSize() {
      int size = 0;
      if (Id != 0D) {
        size += 1 + 8;
      }
      if (InterconnectAttachment.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(InterconnectAttachment);
      }
      if (IpAddress.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(IpAddress);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(ComputeHaVpnGatewayXVpnInterfaces other) {
      if (other == null) {
        return;
      }
      if (other.Id != 0D) {
        Id = other.Id;
      }
      if (other.InterconnectAttachment.Length != 0) {
        InterconnectAttachment = other.InterconnectAttachment;
      }
      if (other.IpAddress.Length != 0) {
        IpAddress = other.IpAddress;
      }
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
          case 9: {
            Id = input.ReadDouble();
            break;
          }
          case 18: {
            InterconnectAttachment = input.ReadString();
            break;
          }
          case 26: {
            IpAddress = input.ReadString();
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
          case 9: {
            Id = input.ReadDouble();
            break;
          }
          case 18: {
            InterconnectAttachment = input.ReadString();
            break;
          }
          case 26: {
            IpAddress = input.ReadString();
            break;
          }
        }
      }
    }
    #endif

  }

  public sealed partial class ComputeHaVpnGateway : pb::IMessage<ComputeHaVpnGateway>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<ComputeHaVpnGateway> _parser = new pb::MessageParser<ComputeHaVpnGateway>(() => new ComputeHaVpnGateway());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pb::MessageParser<ComputeHaVpnGateway> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Oak9.Tython.Gcp.ComputeHa.GcpComputeHaReflection.Descriptor.MessageTypes[2]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public ComputeHaVpnGateway() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public ComputeHaVpnGateway(ComputeHaVpnGateway other) : this() {
      description_ = other.description_;
      id_ = other.id_;
      name_ = other.name_;
      network_ = other.network_;
      project_ = other.project_;
      region_ = other.region_;
      selfLink_ = other.selfLink_;
      timeouts_ = other.timeouts_ != null ? other.timeouts_.Clone() : null;
      vpnInterfaces_ = other.vpnInterfaces_.Clone();
      resourceInfo_ = other.resourceInfo_ != null ? other.resourceInfo_.Clone() : null;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public ComputeHaVpnGateway Clone() {
      return new ComputeHaVpnGateway(this);
    }

    /// <summary>Field number for the "description" field.</summary>
    public const int DescriptionFieldNumber = 1;
    private string description_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Description {
      get { return description_; }
      set {
        description_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "id" field.</summary>
    public const int IdFieldNumber = 2;
    private string id_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Id {
      get { return id_; }
      set {
        id_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "name" field.</summary>
    public const int NameFieldNumber = 3;
    private string name_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Name {
      get { return name_; }
      set {
        name_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "network" field.</summary>
    public const int NetworkFieldNumber = 4;
    private string network_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Network {
      get { return network_; }
      set {
        network_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "project" field.</summary>
    public const int ProjectFieldNumber = 5;
    private string project_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Project {
      get { return project_; }
      set {
        project_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "region" field.</summary>
    public const int RegionFieldNumber = 6;
    private string region_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Region {
      get { return region_; }
      set {
        region_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "self_link" field.</summary>
    public const int SelfLinkFieldNumber = 7;
    private string selfLink_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string SelfLink {
      get { return selfLink_; }
      set {
        selfLink_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "timeouts" field.</summary>
    public const int TimeoutsFieldNumber = 8;
    private global::Oak9.Tython.Gcp.ComputeHa.ComputeHaVpnGatewayXTimeouts timeouts_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public global::Oak9.Tython.Gcp.ComputeHa.ComputeHaVpnGatewayXTimeouts Timeouts {
      get { return timeouts_; }
      set {
        timeouts_ = value;
      }
    }

    /// <summary>Field number for the "vpn_interfaces" field.</summary>
    public const int VpnInterfacesFieldNumber = 9;
    private static readonly pb::FieldCodec<global::Oak9.Tython.Gcp.ComputeHa.ComputeHaVpnGatewayXVpnInterfaces> _repeated_vpnInterfaces_codec
        = pb::FieldCodec.ForMessage(74, global::Oak9.Tython.Gcp.ComputeHa.ComputeHaVpnGatewayXVpnInterfaces.Parser);
    private readonly pbc::RepeatedField<global::Oak9.Tython.Gcp.ComputeHa.ComputeHaVpnGatewayXVpnInterfaces> vpnInterfaces_ = new pbc::RepeatedField<global::Oak9.Tython.Gcp.ComputeHa.ComputeHaVpnGatewayXVpnInterfaces>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::RepeatedField<global::Oak9.Tython.Gcp.ComputeHa.ComputeHaVpnGatewayXVpnInterfaces> VpnInterfaces {
      get { return vpnInterfaces_; }
    }

    /// <summary>Field number for the "resource_info" field.</summary>
    public const int ResourceInfoFieldNumber = 10;
    private global::Oak9.Tython.Shared.ResourceInfo resourceInfo_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public global::Oak9.Tython.Shared.ResourceInfo ResourceInfo {
      get { return resourceInfo_; }
      set {
        resourceInfo_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override bool Equals(object other) {
      return Equals(other as ComputeHaVpnGateway);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public bool Equals(ComputeHaVpnGateway other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (Description != other.Description) return false;
      if (Id != other.Id) return false;
      if (Name != other.Name) return false;
      if (Network != other.Network) return false;
      if (Project != other.Project) return false;
      if (Region != other.Region) return false;
      if (SelfLink != other.SelfLink) return false;
      if (!object.Equals(Timeouts, other.Timeouts)) return false;
      if(!vpnInterfaces_.Equals(other.vpnInterfaces_)) return false;
      if (!object.Equals(ResourceInfo, other.ResourceInfo)) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override int GetHashCode() {
      int hash = 1;
      if (Description.Length != 0) hash ^= Description.GetHashCode();
      if (Id.Length != 0) hash ^= Id.GetHashCode();
      if (Name.Length != 0) hash ^= Name.GetHashCode();
      if (Network.Length != 0) hash ^= Network.GetHashCode();
      if (Project.Length != 0) hash ^= Project.GetHashCode();
      if (Region.Length != 0) hash ^= Region.GetHashCode();
      if (SelfLink.Length != 0) hash ^= SelfLink.GetHashCode();
      if (timeouts_ != null) hash ^= Timeouts.GetHashCode();
      hash ^= vpnInterfaces_.GetHashCode();
      if (resourceInfo_ != null) hash ^= ResourceInfo.GetHashCode();
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
      if (Description.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(Description);
      }
      if (Id.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(Id);
      }
      if (Name.Length != 0) {
        output.WriteRawTag(26);
        output.WriteString(Name);
      }
      if (Network.Length != 0) {
        output.WriteRawTag(34);
        output.WriteString(Network);
      }
      if (Project.Length != 0) {
        output.WriteRawTag(42);
        output.WriteString(Project);
      }
      if (Region.Length != 0) {
        output.WriteRawTag(50);
        output.WriteString(Region);
      }
      if (SelfLink.Length != 0) {
        output.WriteRawTag(58);
        output.WriteString(SelfLink);
      }
      if (timeouts_ != null) {
        output.WriteRawTag(66);
        output.WriteMessage(Timeouts);
      }
      vpnInterfaces_.WriteTo(output, _repeated_vpnInterfaces_codec);
      if (resourceInfo_ != null) {
        output.WriteRawTag(82);
        output.WriteMessage(ResourceInfo);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      if (Description.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(Description);
      }
      if (Id.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(Id);
      }
      if (Name.Length != 0) {
        output.WriteRawTag(26);
        output.WriteString(Name);
      }
      if (Network.Length != 0) {
        output.WriteRawTag(34);
        output.WriteString(Network);
      }
      if (Project.Length != 0) {
        output.WriteRawTag(42);
        output.WriteString(Project);
      }
      if (Region.Length != 0) {
        output.WriteRawTag(50);
        output.WriteString(Region);
      }
      if (SelfLink.Length != 0) {
        output.WriteRawTag(58);
        output.WriteString(SelfLink);
      }
      if (timeouts_ != null) {
        output.WriteRawTag(66);
        output.WriteMessage(Timeouts);
      }
      vpnInterfaces_.WriteTo(ref output, _repeated_vpnInterfaces_codec);
      if (resourceInfo_ != null) {
        output.WriteRawTag(82);
        output.WriteMessage(ResourceInfo);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public int CalculateSize() {
      int size = 0;
      if (Description.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Description);
      }
      if (Id.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Id);
      }
      if (Name.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Name);
      }
      if (Network.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Network);
      }
      if (Project.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Project);
      }
      if (Region.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Region);
      }
      if (SelfLink.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(SelfLink);
      }
      if (timeouts_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(Timeouts);
      }
      size += vpnInterfaces_.CalculateSize(_repeated_vpnInterfaces_codec);
      if (resourceInfo_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(ResourceInfo);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(ComputeHaVpnGateway other) {
      if (other == null) {
        return;
      }
      if (other.Description.Length != 0) {
        Description = other.Description;
      }
      if (other.Id.Length != 0) {
        Id = other.Id;
      }
      if (other.Name.Length != 0) {
        Name = other.Name;
      }
      if (other.Network.Length != 0) {
        Network = other.Network;
      }
      if (other.Project.Length != 0) {
        Project = other.Project;
      }
      if (other.Region.Length != 0) {
        Region = other.Region;
      }
      if (other.SelfLink.Length != 0) {
        SelfLink = other.SelfLink;
      }
      if (other.timeouts_ != null) {
        if (timeouts_ == null) {
          Timeouts = new global::Oak9.Tython.Gcp.ComputeHa.ComputeHaVpnGatewayXTimeouts();
        }
        Timeouts.MergeFrom(other.Timeouts);
      }
      vpnInterfaces_.Add(other.vpnInterfaces_);
      if (other.resourceInfo_ != null) {
        if (resourceInfo_ == null) {
          ResourceInfo = new global::Oak9.Tython.Shared.ResourceInfo();
        }
        ResourceInfo.MergeFrom(other.ResourceInfo);
      }
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
            Description = input.ReadString();
            break;
          }
          case 18: {
            Id = input.ReadString();
            break;
          }
          case 26: {
            Name = input.ReadString();
            break;
          }
          case 34: {
            Network = input.ReadString();
            break;
          }
          case 42: {
            Project = input.ReadString();
            break;
          }
          case 50: {
            Region = input.ReadString();
            break;
          }
          case 58: {
            SelfLink = input.ReadString();
            break;
          }
          case 66: {
            if (timeouts_ == null) {
              Timeouts = new global::Oak9.Tython.Gcp.ComputeHa.ComputeHaVpnGatewayXTimeouts();
            }
            input.ReadMessage(Timeouts);
            break;
          }
          case 74: {
            vpnInterfaces_.AddEntriesFrom(input, _repeated_vpnInterfaces_codec);
            break;
          }
          case 82: {
            if (resourceInfo_ == null) {
              ResourceInfo = new global::Oak9.Tython.Shared.ResourceInfo();
            }
            input.ReadMessage(ResourceInfo);
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
            Description = input.ReadString();
            break;
          }
          case 18: {
            Id = input.ReadString();
            break;
          }
          case 26: {
            Name = input.ReadString();
            break;
          }
          case 34: {
            Network = input.ReadString();
            break;
          }
          case 42: {
            Project = input.ReadString();
            break;
          }
          case 50: {
            Region = input.ReadString();
            break;
          }
          case 58: {
            SelfLink = input.ReadString();
            break;
          }
          case 66: {
            if (timeouts_ == null) {
              Timeouts = new global::Oak9.Tython.Gcp.ComputeHa.ComputeHaVpnGatewayXTimeouts();
            }
            input.ReadMessage(Timeouts);
            break;
          }
          case 74: {
            vpnInterfaces_.AddEntriesFrom(ref input, _repeated_vpnInterfaces_codec);
            break;
          }
          case 82: {
            if (resourceInfo_ == null) {
              ResourceInfo = new global::Oak9.Tython.Shared.ResourceInfo();
            }
            input.ReadMessage(ResourceInfo);
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
