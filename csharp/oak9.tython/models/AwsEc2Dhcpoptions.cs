// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: aws/aws_ec2_dhcpoptions.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021, 8981
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace Oak9.Tython.Aws.Ec2Dhcpoptions {

  /// <summary>Holder for reflection information generated from aws/aws_ec2_dhcpoptions.proto</summary>
  public static partial class AwsEc2DhcpoptionsReflection {

    #region Descriptor
    /// <summary>File descriptor for aws/aws_ec2_dhcpoptions.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static AwsEc2DhcpoptionsReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "Ch1hd3MvYXdzX2VjMl9kaGNwb3B0aW9ucy5wcm90bxIfb2FrOS50eXRob24u",
            "YXdzLmVjMl9kaGNwb3B0aW9ucxoTc2hhcmVkL3NoYXJlZC5wcm90byK5AgoL",
            "REhDUE9wdGlvbnMSNwoNcmVzb3VyY2VfaW5mbxgBIAEoCzIgLm9hazkudHl0",
            "aG9uLnNoYXJlZC5SZXNvdXJjZUluZm8SEwoLZG9tYWluX25hbWUYAiABKAkS",
            "GwoTZG9tYWluX25hbWVfc2VydmVycxgDIAMoCRIcChRuZXRiaW9zX25hbWVf",
            "c2VydmVycxgEIAMoCRIZChFuZXRiaW9zX25vZGVfdHlwZRgFIAEoBRITCgtu",
            "dHBfc2VydmVycxgGIAMoCRJECgR0YWdzGAcgAygLMjYub2FrOS50eXRob24u",
            "YXdzLmVjMl9kaGNwb3B0aW9ucy5ESENQT3B0aW9ucy5UYWdzRW50cnkaKwoJ",
            "VGFnc0VudHJ5EgsKA2tleRgBIAEoCRINCgV2YWx1ZRgCIAEoCToCOAEiVQoP",
            "RUMyX0RIQ1BPcHRpb25zEkIKDGRoY3Bfb3B0aW9ucxgBIAEoCzIsLm9hazku",
            "dHl0aG9uLmF3cy5lYzJfZGhjcG9wdGlvbnMuREhDUE9wdGlvbnNiBnByb3Rv",
            "Mw=="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { global::Oak9.Tython.Shared.SharedReflection.Descriptor, },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::Oak9.Tython.Aws.Ec2Dhcpoptions.DHCPOptions), global::Oak9.Tython.Aws.Ec2Dhcpoptions.DHCPOptions.Parser, new[]{ "ResourceInfo", "DomainName", "DomainNameServers", "NetbiosNameServers", "NetbiosNodeType", "NtpServers", "Tags" }, null, null, null, new pbr::GeneratedClrTypeInfo[] { null, }),
            new pbr::GeneratedClrTypeInfo(typeof(global::Oak9.Tython.Aws.Ec2Dhcpoptions.EC2_DHCPOptions), global::Oak9.Tython.Aws.Ec2Dhcpoptions.EC2_DHCPOptions.Parser, new[]{ "DhcpOptions" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class DHCPOptions : pb::IMessage<DHCPOptions>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<DHCPOptions> _parser = new pb::MessageParser<DHCPOptions>(() => new DHCPOptions());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pb::MessageParser<DHCPOptions> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Oak9.Tython.Aws.Ec2Dhcpoptions.AwsEc2DhcpoptionsReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public DHCPOptions() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public DHCPOptions(DHCPOptions other) : this() {
      resourceInfo_ = other.resourceInfo_ != null ? other.resourceInfo_.Clone() : null;
      domainName_ = other.domainName_;
      domainNameServers_ = other.domainNameServers_.Clone();
      netbiosNameServers_ = other.netbiosNameServers_.Clone();
      netbiosNodeType_ = other.netbiosNodeType_;
      ntpServers_ = other.ntpServers_.Clone();
      tags_ = other.tags_.Clone();
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public DHCPOptions Clone() {
      return new DHCPOptions(this);
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

    /// <summary>Field number for the "domain_name" field.</summary>
    public const int DomainNameFieldNumber = 2;
    private string domainName_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string DomainName {
      get { return domainName_; }
      set {
        domainName_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "domain_name_servers" field.</summary>
    public const int DomainNameServersFieldNumber = 3;
    private static readonly pb::FieldCodec<string> _repeated_domainNameServers_codec
        = pb::FieldCodec.ForString(26);
    private readonly pbc::RepeatedField<string> domainNameServers_ = new pbc::RepeatedField<string>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::RepeatedField<string> DomainNameServers {
      get { return domainNameServers_; }
    }

    /// <summary>Field number for the "netbios_name_servers" field.</summary>
    public const int NetbiosNameServersFieldNumber = 4;
    private static readonly pb::FieldCodec<string> _repeated_netbiosNameServers_codec
        = pb::FieldCodec.ForString(34);
    private readonly pbc::RepeatedField<string> netbiosNameServers_ = new pbc::RepeatedField<string>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::RepeatedField<string> NetbiosNameServers {
      get { return netbiosNameServers_; }
    }

    /// <summary>Field number for the "netbios_node_type" field.</summary>
    public const int NetbiosNodeTypeFieldNumber = 5;
    private int netbiosNodeType_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public int NetbiosNodeType {
      get { return netbiosNodeType_; }
      set {
        netbiosNodeType_ = value;
      }
    }

    /// <summary>Field number for the "ntp_servers" field.</summary>
    public const int NtpServersFieldNumber = 6;
    private static readonly pb::FieldCodec<string> _repeated_ntpServers_codec
        = pb::FieldCodec.ForString(50);
    private readonly pbc::RepeatedField<string> ntpServers_ = new pbc::RepeatedField<string>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::RepeatedField<string> NtpServers {
      get { return ntpServers_; }
    }

    /// <summary>Field number for the "tags" field.</summary>
    public const int TagsFieldNumber = 7;
    private static readonly pbc::MapField<string, string>.Codec _map_tags_codec
        = new pbc::MapField<string, string>.Codec(pb::FieldCodec.ForString(10, ""), pb::FieldCodec.ForString(18, ""), 58);
    private readonly pbc::MapField<string, string> tags_ = new pbc::MapField<string, string>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::MapField<string, string> Tags {
      get { return tags_; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override bool Equals(object other) {
      return Equals(other as DHCPOptions);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public bool Equals(DHCPOptions other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (!object.Equals(ResourceInfo, other.ResourceInfo)) return false;
      if (DomainName != other.DomainName) return false;
      if(!domainNameServers_.Equals(other.domainNameServers_)) return false;
      if(!netbiosNameServers_.Equals(other.netbiosNameServers_)) return false;
      if (NetbiosNodeType != other.NetbiosNodeType) return false;
      if(!ntpServers_.Equals(other.ntpServers_)) return false;
      if (!Tags.Equals(other.Tags)) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override int GetHashCode() {
      int hash = 1;
      if (resourceInfo_ != null) hash ^= ResourceInfo.GetHashCode();
      if (DomainName.Length != 0) hash ^= DomainName.GetHashCode();
      hash ^= domainNameServers_.GetHashCode();
      hash ^= netbiosNameServers_.GetHashCode();
      if (NetbiosNodeType != 0) hash ^= NetbiosNodeType.GetHashCode();
      hash ^= ntpServers_.GetHashCode();
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
      if (DomainName.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(DomainName);
      }
      domainNameServers_.WriteTo(output, _repeated_domainNameServers_codec);
      netbiosNameServers_.WriteTo(output, _repeated_netbiosNameServers_codec);
      if (NetbiosNodeType != 0) {
        output.WriteRawTag(40);
        output.WriteInt32(NetbiosNodeType);
      }
      ntpServers_.WriteTo(output, _repeated_ntpServers_codec);
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
      if (DomainName.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(DomainName);
      }
      domainNameServers_.WriteTo(ref output, _repeated_domainNameServers_codec);
      netbiosNameServers_.WriteTo(ref output, _repeated_netbiosNameServers_codec);
      if (NetbiosNodeType != 0) {
        output.WriteRawTag(40);
        output.WriteInt32(NetbiosNodeType);
      }
      ntpServers_.WriteTo(ref output, _repeated_ntpServers_codec);
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
      if (DomainName.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(DomainName);
      }
      size += domainNameServers_.CalculateSize(_repeated_domainNameServers_codec);
      size += netbiosNameServers_.CalculateSize(_repeated_netbiosNameServers_codec);
      if (NetbiosNodeType != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(NetbiosNodeType);
      }
      size += ntpServers_.CalculateSize(_repeated_ntpServers_codec);
      size += tags_.CalculateSize(_map_tags_codec);
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(DHCPOptions other) {
      if (other == null) {
        return;
      }
      if (other.resourceInfo_ != null) {
        if (resourceInfo_ == null) {
          ResourceInfo = new global::Oak9.Tython.Shared.ResourceInfo();
        }
        ResourceInfo.MergeFrom(other.ResourceInfo);
      }
      if (other.DomainName.Length != 0) {
        DomainName = other.DomainName;
      }
      domainNameServers_.Add(other.domainNameServers_);
      netbiosNameServers_.Add(other.netbiosNameServers_);
      if (other.NetbiosNodeType != 0) {
        NetbiosNodeType = other.NetbiosNodeType;
      }
      ntpServers_.Add(other.ntpServers_);
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
            DomainName = input.ReadString();
            break;
          }
          case 26: {
            domainNameServers_.AddEntriesFrom(input, _repeated_domainNameServers_codec);
            break;
          }
          case 34: {
            netbiosNameServers_.AddEntriesFrom(input, _repeated_netbiosNameServers_codec);
            break;
          }
          case 40: {
            NetbiosNodeType = input.ReadInt32();
            break;
          }
          case 50: {
            ntpServers_.AddEntriesFrom(input, _repeated_ntpServers_codec);
            break;
          }
          case 58: {
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
            DomainName = input.ReadString();
            break;
          }
          case 26: {
            domainNameServers_.AddEntriesFrom(ref input, _repeated_domainNameServers_codec);
            break;
          }
          case 34: {
            netbiosNameServers_.AddEntriesFrom(ref input, _repeated_netbiosNameServers_codec);
            break;
          }
          case 40: {
            NetbiosNodeType = input.ReadInt32();
            break;
          }
          case 50: {
            ntpServers_.AddEntriesFrom(ref input, _repeated_ntpServers_codec);
            break;
          }
          case 58: {
            tags_.AddEntriesFrom(ref input, _map_tags_codec);
            break;
          }
        }
      }
    }
    #endif

  }

  public sealed partial class EC2_DHCPOptions : pb::IMessage<EC2_DHCPOptions>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<EC2_DHCPOptions> _parser = new pb::MessageParser<EC2_DHCPOptions>(() => new EC2_DHCPOptions());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pb::MessageParser<EC2_DHCPOptions> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Oak9.Tython.Aws.Ec2Dhcpoptions.AwsEc2DhcpoptionsReflection.Descriptor.MessageTypes[1]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public EC2_DHCPOptions() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public EC2_DHCPOptions(EC2_DHCPOptions other) : this() {
      dhcpOptions_ = other.dhcpOptions_ != null ? other.dhcpOptions_.Clone() : null;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public EC2_DHCPOptions Clone() {
      return new EC2_DHCPOptions(this);
    }

    /// <summary>Field number for the "dhcp_options" field.</summary>
    public const int DhcpOptionsFieldNumber = 1;
    private global::Oak9.Tython.Aws.Ec2Dhcpoptions.DHCPOptions dhcpOptions_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public global::Oak9.Tython.Aws.Ec2Dhcpoptions.DHCPOptions DhcpOptions {
      get { return dhcpOptions_; }
      set {
        dhcpOptions_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override bool Equals(object other) {
      return Equals(other as EC2_DHCPOptions);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public bool Equals(EC2_DHCPOptions other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (!object.Equals(DhcpOptions, other.DhcpOptions)) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override int GetHashCode() {
      int hash = 1;
      if (dhcpOptions_ != null) hash ^= DhcpOptions.GetHashCode();
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
      if (dhcpOptions_ != null) {
        output.WriteRawTag(10);
        output.WriteMessage(DhcpOptions);
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
      if (dhcpOptions_ != null) {
        output.WriteRawTag(10);
        output.WriteMessage(DhcpOptions);
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
      if (dhcpOptions_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(DhcpOptions);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(EC2_DHCPOptions other) {
      if (other == null) {
        return;
      }
      if (other.dhcpOptions_ != null) {
        if (dhcpOptions_ == null) {
          DhcpOptions = new global::Oak9.Tython.Aws.Ec2Dhcpoptions.DHCPOptions();
        }
        DhcpOptions.MergeFrom(other.DhcpOptions);
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
            if (dhcpOptions_ == null) {
              DhcpOptions = new global::Oak9.Tython.Aws.Ec2Dhcpoptions.DHCPOptions();
            }
            input.ReadMessage(DhcpOptions);
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
            if (dhcpOptions_ == null) {
              DhcpOptions = new global::Oak9.Tython.Aws.Ec2Dhcpoptions.DHCPOptions();
            }
            input.ReadMessage(DhcpOptions);
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